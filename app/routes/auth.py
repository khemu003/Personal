from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User, Contact, Feedback, Transaction, TransactionType
from app import db
from datetime import datetime

auth_bp = Blueprint('auth', __name__)
dashboard_bp = Blueprint('dashboard', __name__)

@auth_bp.route('/')
def home():
    return render_template('index.html')

@auth_bp.route('/contact', methods=['Get', 'Post'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()
        flash('Add contact successfuly')

    return render_template('contact.html')

@auth_bp.route('/feedback', methods=['Get', 'Post'])
@login_required
def feedback():
    if request.method == 'POST':
        experience = request.form['experience']
        rating = request.form['rating']

        new_feedback = Feedback(user_id=current_user.id, content=experience, rating=rating)
        db.session.add(new_feedback)
        db.session.commit()
    return render_template('feedback.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard.dashboard'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'warning')
            return redirect(url_for('auth.signup'))

        new_user = User(username=username, email=email, password_hash=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html')

@dashboard_bp.route('/add_transaction', methods=['POST'])
@login_required
def add_transaction():
    if request.method == 'POST':
        print(f"➕ Adding transaction for user: {current_user.username} (ID: {current_user.id})")
        date_str = request.form['date']
        description = request.form['description']
        amount = request.form['amount']
        type_str = request.form['type']
        category = request.form.get('category', '')  # Optional category

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            amount = int(amount)
            # Handle the enum conversion more safely
            if type_str.lower() == 'income':
                type_enum = TransactionType.income
            elif type_str.lower() == 'expense':
                type_enum = TransactionType.expense
            else:
                flash('Invalid transaction type', 'danger')
                return redirect(url_for('dashboard.dashboard'))
        except ValueError as e:
            flash(f'Invalid input data: {str(e)}', 'danger')
            return redirect(url_for('dashboard.dashboard'))
        except Exception as e:
            flash(f'Error processing transaction: {str(e)}', 'danger')
            return redirect(url_for('dashboard.dashboard'))

        new_transaction = Transaction(
            user_id=current_user.id,  # Add the user_id
            date=date,
            description=description,
            amount=amount,
            type=type_enum,
            category=category
        )
        
        db.session.add(new_transaction)
        db.session.commit()
        
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('dashboard.dashboard'))
    
    return redirect(url_for('dashboard.dashboard'))

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'info')
    return redirect(url_for('auth.login'))

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # Get user's transactions
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.date.desc()).all()
    return render_template('dashboard/dashboard.html', transactions=transactions)

@dashboard_bp.route('/get_transactions')
@login_required
def get_transactions():
    print(f"🔍 Getting transactions for user: {current_user.username} (ID: {current_user.id})")
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.date.desc()).all()
    print(f"📊 Found {len(transactions)} transactions for user {current_user.username}")
    
    transaction_list = []
    for t in transactions:
        transaction_list.append({
            'id': t.id,
            'date': t.date.strftime('%Y-%m-%d'),
            'description': t.description,
            'amount': t.amount,
            'type': t.type.value,
            'category': t.category or ''
        })
        print(f"  - Transaction: {t.description} (₹{t.amount}, {t.type.value})")
    
    return {'transactions': transaction_list}

@dashboard_bp.route('/delete_transaction/<int:transaction_id>', methods=['POST'])
@login_required
def delete_transaction(transaction_id):
    transaction = Transaction.query.filter_by(id=transaction_id, user_id=current_user.id).first()
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
        return {'success': True, 'message': 'Transaction deleted successfully!'}
    else:
        return {'success': False, 'message': 'Transaction not found!'}, 404


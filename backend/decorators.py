from functools import wraps
from flask import session, redirect, url_for, flash, request, jsonify

def is_api_request():
    # return False  # Simplified for this example; adjust as needed for your application
    return request.path.startswith('/api/') or request.path.startswith('/admin/api/')

def role_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                if is_api_request():
                    return jsonify({'error': 'Authentication required'}), 401
                flash('Please log in to continue.', 'error')
                return redirect(url_for('login'))
            
            if session.get('role', '') not in allowed_roles:
                if is_api_request():
                    return jsonify({'error': 'Insufficient permissions'}), 403
                flash('Access denied for your account role.', 'error')
                return redirect(url_for('login'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

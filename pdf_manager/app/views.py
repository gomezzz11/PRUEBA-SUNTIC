from flask import render_template, redirect, url_for, flash, request, send_from_directory
from flask_login import login_required, current_user
from app import app, db
from app.forms import UploadForm
from app.models import Document, User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    form.approver.choices = [(user.id, user.email) for user in User.query.all()]
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        document = Document(
            title=form.title.data,
            description=form.description.data,
            filename=filename,
            owner=current_user,
            approver_id=form.approver.data
        )
        db.session.add(document)
        db.session.commit()
        flash('Document uploaded successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)

@app.route('/documents')
@login_required
def documents():
    documents = Document.query.filter((Document.owner_id == current_user.id) | (Document.approver_id == current_user.id)).all()
    return render_template('document_list.html', documents=documents)

@app.route('/approve/<int:document_id>', methods=['GET', 'POST'])
@login_required
def approve(document_id):
    document = Document.query.get_or_404(document_id)
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'approve':
            document.status = 'Approved'
        elif action == 'reject':
            document.status = 'Rejected'
        db.session.commit()
        flash('Document status updated!', 'success')
        return redirect(url_for('documents'))
    return render_template('approve.html', document=document)

@app.route('/uploads/<filename>')
@login_required
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

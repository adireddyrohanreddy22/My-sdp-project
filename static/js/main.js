document.addEventListener('DOMContentLoaded', function () {
    // small enhancement: fade-in already handled by CSS animation class
    // add confirm modal for links with data-confirm
    var modalRoot = document.getElementById('modal-root');
    var modalTitle = document.getElementById('modal-title');
    var modalMessage = document.getElementById('modal-message');
    var modalCancel = document.getElementById('modal-cancel');
    var modalConfirm = document.getElementById('modal-confirm');
    var toastRoot = document.getElementById('toast-root');

    function showModal(title, message) {
        modalTitle.textContent = title || 'Confirm';
        modalMessage.textContent = message || 'Are you sure?';
        modalRoot.setAttribute('aria-hidden', 'false');
        modalRoot.classList.add('open');
    }
    function hideModal() { modalRoot.setAttribute('aria-hidden', 'true'); }

    function showToast(text, type) {
        var t = document.createElement('div');
        t.className = 'toast ' + (type || '');
        t.textContent = text;
        toastRoot.appendChild(t);
        setTimeout(function () { t.remove(); }, 3500);
    }

    // attach enhanced delete behavior
    document.querySelectorAll('a[data-confirm]').forEach(function (a) {
        a.addEventListener('click', function (ev) {
            ev.preventDefault();
            var msg = a.getAttribute('data-confirm') || 'Are you sure?';
            var href = a.getAttribute('href');
            showModal('Confirm action', msg);

            function doConfirm() {
                hideModal();
                modalRoot.classList.remove('open');
                // perform POST to delete URL (fetch with CSRF)
                var csrftoken = getCookie('csrftoken');
                fetch(href, { method: 'POST', headers: { 'X-CSRFToken': csrftoken, 'X-Requested-With': 'XMLHttpRequest' } })
                    .then(function (resp) {
                        if (resp.ok) {
                            showToast('Deleted successfully', 'success');
                            setTimeout(function () { location.reload(); }, 700);
                        } else {
                            showToast('Action failed', 'error');
                        }
                    }).catch(function () { showToast('Network error', 'error'); });
            }

            modalConfirm.onclick = doConfirm;
            modalCancel.onclick = hideModal;
        });
    });

    // close modal when clicking backdrop
    var modalBackdrop = document.querySelector('.modal-backdrop');
    if (modalBackdrop) { modalBackdrop.addEventListener('click', function () { hideModal(); modalRoot.classList.remove('open'); }); }

    // simple live search for students
    var search = document.getElementById('student-search');
    if (search) {
        search.addEventListener('input', function () {
            var q = this.value.toLowerCase().trim();
            document.querySelectorAll('.data-table tbody tr').forEach(function (row) {
                var text = row.textContent.toLowerCase();
                row.style.display = text.indexOf(q) === -1 ? 'none' : '';
            });
        });
    }

    // CSRF helper
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

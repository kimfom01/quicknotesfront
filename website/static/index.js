deleteNote = (noteId) => {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId })
    })
    .then((result) => {
        window.location.href ="/"
    })
}
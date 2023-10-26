deleteNote = (noteId) => {
  try {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId }),
    }).then((result) => {
      console.log(result);
      window.location.reload();
    });
  } catch (err) {
    console.error(err);
  }
};

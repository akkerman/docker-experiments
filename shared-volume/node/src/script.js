const app = document.getElementById('app')
fetch('/test')
  .then(result => {
    if (result.ok) {
      return result.json()
    }
    throw result.statusText
  })
  .then(json => {
    app.innerHTML = 'test: ' + json.test + '&nbsp;date: ' + json.date
  })
  .catch(err => {
    app.innerHTML = err
  })

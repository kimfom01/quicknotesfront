# Quick Notes

Organize your thoughts

## Description

<!-- An extended description of your project. Here, explain what your project does, its features, and its purpose. This section is particularly important to give users and contributors an overview of what your project is all about. -->

This is a note taking application that helps you save texts (notes) and soon to be images. It's main purpose is to help store your thought process so that you can organize them and become more productive.

## Getting Started

### Dependencies

Ensure you have [python](https://www.python.org/) installed and access to a database provider like [postgres](https://www.postgresql.org/)

- flask
- Flask-SQLAlchemy
- flask-login
- Authlib
- requests
- Gunicorn

See `back/requirements.txt` for full list of dependenciess

### Installing

In order to get started, follow these steps

#### Step 1: Clone the repo

On your terminal run the following command to clone the repository

```sh
git clone https://github.com/kimfom01/quicknotes.git
```

#### Step 2: Go to back directory

Navigate to the `back` directory

```sh
cd back/
```

#### Step 3: Install required packages

```sh
pip install -r requirements.txt
```

#### Step 4: Create .env

The project depends on some config that it expects to be provided from a .env file at the `back` directory.  
Here is the structure of the file

```env
OAUTH2_CLIENT_ID=
OAUTH2_CLIENT_SECRET=
OAUTH2_META_URL=
FLASK_SECRET=
DB_URI=
DEMO_USERNAME=
```

#### Step 5: Run Migrations

```sh
flask db init
flask db migrate
flask db upgrade
```

### Executing program

Within the `back` directory

```sh
python main.py
```

## Hosting

- [Render](https://render.com/)

## Database Provider

- Postgres through [neon.tech](https://neon.tech/)

<!-- ## Help

Any advice for common problems or issues.
command to run if program contains helper info -->

## Authors

Contributors names and contact info

- Kim Fom - [kimfom01@gmail.com](mailto:kimfom01@gmail.com)

<!-- ## Version History

- 0.2
  - Various bug fixes and optimizations
  - See [commit change]() or [release history]()
- 0.1
  - Initial Release -->

<!-- ## License

This project is licensed under the [LICENSE NAME] License - see the LICENSE.md file for details -->

<!-- ## Acknowledgments

Give credit to any resources or individuals that helped in the development of this project.

- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [Markdown Syntax Guide](https://www.markdownguide.org/basic-syntax/)
- [Choose an Open Source License](https://choosealicense.com/) -->

## Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

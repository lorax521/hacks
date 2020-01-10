set /p app="Enter app name: "
npx create-react-app %app%
cd %app%
npm install --save redux
npm install --save @material-ui/core
npm install --save @material-ui/icons
npm install --save typeface-roboto
mkdir src
mkdir src/assets
mkdir src/assets/images
mkdir src/app
mkdir src/app/actions
mkdir src/app/components
mkdir src/app/reducers
mkdir src/app/services

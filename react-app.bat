set /p app="Enter app name: "
npx create-react-app %app%
cd %app%
npm install --save redux
npm install --save @material-ui/core
npm install --save @material-ui/icons
npm install --save typeface-roboto

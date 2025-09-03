
useful links here

For streamlit : the application uses google material icons : refer :  https://fonts.google.com/icons

Run application :

streamlit run main.py

### Building the custom sidebar component

The app depends on a custom component in `sidebar_component/sidebar_comp`. If you see
`StreamlitAPIException: No such component directory` when running the app, build the
component frontend first:

```
cd sidebar_component/sidebar_comp/frontend
npm install
npm run build
```

After the build step a `frontend/build` directory will be created and the component
can be loaded by Streamlit.


mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"korelin.ivan@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
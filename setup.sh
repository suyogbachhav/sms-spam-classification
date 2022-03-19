mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORTt\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
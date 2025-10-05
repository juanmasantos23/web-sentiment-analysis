CREATE TABLE IF NOT EXISTS web_kpis (
    id SERIAL PRIMARY KEY,
    date DATE,
    visits INT,
    conversions INT,
    traffic_source VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS social_sentiment (
    id SERIAL PRIMARY KEY,
    date DATE,
    platform VARCHAR(50),
    sentiment_score DECIMAL,
    text_content TEXT
);

This week we’re exploring **Brazilian Companies**, curated from Brazil’s open **CNPJ (Cadastro Nacional da Pessoa Jurídica)** records published by the **Brazilian Ministry of Finance / Receita Federal** on the national open-data portal ([dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj)).

> The CNPJ open data is a large-scale public registry of Brazilian legal entities. For this dataset, the raw company records were cleaned and enriched with lookup tables (legal nature, owner qualification, and company size), then filtered to retain firms above a share-capital threshold so the analysis focuses on meaningful variation in capital stock.

- Which **legal nature** categories concentrate the highest total and average capital stock?
  LLC and Publicly Traded Companies concentrate at the top
- How does **company size** relate to capital stock (and how skewed is it)?

  Company size has little impact on capital stock, but for all sizes, there is heavy left-skew. This means that for most companies have capital stocks less than the mean, 688,146.30.

- Do specific **owner qualification** groups dominate high-capital companies?
  Managing Partners/Partner-Administrator appears the most frequently, followed by Administrator/Manager
- What patterns emerge when comparing the **top capital-stock tail** across categories (legal nature, size, qualification)?
  Top stock companies tend to be LLCs with Managing Partners and are of company size 'other'

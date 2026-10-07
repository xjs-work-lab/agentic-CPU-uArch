# views

Generated/derived views. Generated relations never become authority.

- graph/current.json — bidirectional navigation projection: canonical semantic edges + generated reverse edges.
- graph/dependency.json — single-direction derived dependency/inference projection for graph algorithms.

Use dependency.json, not current.json, for centrality/path/bridge analyses that assume edge direction has inferential meaning.

# Trust records

Les fichiers `.content/trust/<slug>.json` sont la source de vérité des pages de confiance du site.

## Pages couvertes

- `methode-de-test` → `METHODOLOGY`
- `comment-nous-comparons` → `COMPARISON_POLICY`
- `a-propos` → `ABOUT`
- `contact` → `CONTACT`
- `transparence-affiliation` → `AFFILIATE_DISCLOSURE`
- `mentions-legales` → `LEGAL_PENDING` jusqu'à réception des informations légales confirmées

## État éditorial actuel

- `methode-de-test` : `DRAFT_READY` — page rédigée comme méthode d'évaluation, sans revendiquer de test physique non documenté.
- `comment-nous-comparons` : `DRAFT_READY` — critères, preuves, pondération, scoring, hard gates, données manquantes et affiliation documentés.
- `transparence-affiliation` : `DRAFT_READY` — fonctionnement de l'affiliation et séparation avec le ranking documentés ; programmes actifs et politique sur prêts/sponsoring restent explicitement inconnus.
- `a-propos` : `NEEDS_OWNER_INPUT` — placeholder neutralisé, sans fausse équipe ni faux test.
- `contact` : `NEEDS_OWNER_INPUT` — coordonnées ou mécanisme de contact à confirmer.
- `mentions-legales` : `LEGAL_PENDING` — aucune donnée juridique ne doit être inventée.

## Principe

Ne jamais corriger uniquement le HTML lorsqu'une affirmation touche à :

- l'identité du site ou de son éditeur ;
- l'existence de tests physiques ;
- une équipe ou des contributeurs ;
- l'indépendance éditoriale ;
- l'affiliation ;
- les relations avec les marques ;
- les coordonnées de contact ;
- les informations juridiques.

Mettre d'abord à jour le registre de vérité, puis rédiger la page.

## Niveaux de preuve

- `DIRECT_OBSERVATION`
- `REPO_EVIDENCE`
- `OFFICIAL_SOURCE`
- `OWNER_CONFIRMED`
- `EDITORIAL_INFERENCE`
- `UNKNOWN`

## Statuts

- `READY_FOR_DRAFT` : suffisamment d'informations pour produire une première version.
- `NEEDS_OWNER_INPUT` : des informations institutionnelles doivent être confirmées avant rédaction complète.
- `DRAFT_READY` : texte produit, QA pas encore approuvée.
- `HUMAN_APPROVED` : contenu validé humainement ; l'indexation reste une décision distincte.
- `LEGAL_PENDING` : données légales manquantes ; aucune rédaction juridique ne doit être inventée.

## Règle de publication

`HUMAN_APPROVED` n'enlève jamais automatiquement `noindex,follow`.

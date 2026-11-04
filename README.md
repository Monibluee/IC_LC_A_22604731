# Mochila do Aventureiro

**Julia Holanda** — 22604731

Um programa em Python para gerir os itens que o aventureiro guarda na mochila, de forma **simples** e *interativa*.

## Como correr

Na pasta do projeto, executa:

```bash
python mochila.py
```

Se o teu sistema usar `python3` para executar Python, podes usar:

```bash
python3 mochila.py
```

## Itens iniciais

| Item | Peso | Peso em binário |
|---|---:|---:|
| Espada | 8 kg | 1000 |
| Escudo | 10 kg | 1010 |
| Poção | 1 kg | 1 |

## Fluxograma

```mermaid
flowchart TD
    A[Opção 2 escolhida] --> B{Há itens disponíveis?}
    B -->|Não| C[Mostrar: Não há mais itens para guardar]
    C --> Z[Fim]
    B -->|Sim| D[Mostrar itens disponíveis]
    D --> E[Pedir o índice do item]
    E --> F{A escolha contém apenas dígitos?}
    F -->|Não| G[Mostrar: Opção inválida]
    G --> Z
    F -->|Sim| H{O índice está dentro da lista?}
    H -->|Não| G
    H -->|Sim| I{O peso do item é superior a 20 kg?}
    I -->|Sim| J[Mostrar: O item é demasiado pesado]
    J --> Z
    I -->|Não| K{O peso total ultrapassa 30 kg?}
    K -->|Sim| L[Mostrar: A mochila está cheia]
    L --> Z
    K -->|Não| M[Guardar o item na mochila e removê-lo dos disponíveis]
    M --> N[Mostrar confirmação]
    N --> Z
```

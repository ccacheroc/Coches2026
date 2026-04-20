# Manual de GitHub Copilot — Guía completa de uso

> Documento de referencia generado a partir de la configuración real del proyecto **Coches2026**.
> Cubre desde los conceptos básicos hasta la organización avanzada de contexto para agentes de IA.

---

## Índice

1. [Qué es GitHub Copilot y sus modos de uso](#1-qué-es-github-copilot-y-sus-modos-de-uso)
2. [Los tres mecanismos de interacción: `#`, `@`, `/`](#2-los-tres-mecanismos-de-interacción)
3. [Herramientas (tools) predefinidas del agente](#3-herramientas-tools-predefinidas-del-agente)
4. [Estructura de `.github/` para guiar a Copilot](#4-estructura-de-github-para-guiar-a-copilot)
5. [Instruction files — activación automática](#5-instruction-files--activación-automática)
6. [Prompt files — invocación manual](#6-prompt-files--invocación-manual)
7. [AGENTS.md vs copilot-instructions.md](#7-agentsmd-vs-copilot-instructionsmd)
8. [MCP — ampliar las herramientas del agente](#8-mcp--ampliar-las-herramientas-del-agente)
9. [Configuración real de este proyecto (Coches2026)](#9-configuración-real-de-este-proyecto-coches2026)
10. [Recetas de uso habitual](#10-recetas-de-uso-habitual)

---

## 1. Qué es GitHub Copilot y sus modos de uso

GitHub Copilot ofrece tres modos principales:

| Modo | Dónde | Qué hace |
|---|---|---|
| **Completado inline** | Editor de código | Sugiere continuaciones de código mientras escribes |
| **Chat** | Panel lateral / ventana de chat | Conversación para preguntar, explicar, generar |
| **Agente (Agent mode)** | Chat con agent mode activado | Ejecuta tareas autónomas: lee ficheros, edita, corre tests, corrige errores en bucle |

El **modo agente** es el más potente: encadena herramientas de forma autónoma hasta resolver la tarea completa sin intervención manual en cada paso.

---

## 2. Los tres mecanismos de interacción

En el chat de Copilot hay tres tipos de elementos que modifican el comportamiento de la respuesta. Se pueden combinar en el mismo mensaje.

### `#` — Referencias de contexto

Sirven para **adjuntar contexto** a tu mensaje. Copilot incluye ese contenido en la conversación.

| Variable | Qué adjunta |
|---|---|
| `#file` | Un fichero concreto del workspace |
| `#selection` | El texto seleccionado en el editor |
| `#editor` | El fichero abierto actualmente |
| `#terminalLastCommand` | El último comando ejecutado en la terminal |
| `#terminalSelection` | El texto seleccionado en la terminal |
| `#codebase` | Búsqueda semántica en todo el repositorio |
| `#sym` | Un símbolo concreto (clase, función, variable…) |
| `#problems` | Los errores activos del panel de problemas del IDE |
| `#<nombre>` | Un fichero `.prompt.md` de `.github/prompts/` |

**Ejemplo:**
```
Explica por qué falla #terminalLastCommand mirando #file:entities/coche.py
```

### `@` — Agentes (Participants)

Cambian **quién responde**: redirigen la consulta a un agente especializado con herramientas propias.

| Agente | Para qué sirve |
|---|---|
| `@workspace` | Consultas sobre todo el repositorio (busca en el codebase) |
| `@vscode` | Preguntas sobre configuración y comandos de VS Code |
| `@terminal` | Ayuda con comandos de shell y errores de terminal |
| `@github` | Búsquedas en GitHub (PRs, issues, repos) — requiere extensión |

Los `@` son extensibles: empresas y terceros pueden publicar extensiones en el Marketplace que añaden nuevos participantes (`@docker`, `@azure`, `@stripe`, etc.).

### `/` — Comandos (Slash commands)

Activan un **modo de comportamiento predefinido**. Son atajos para tareas comunes.

#### Comandos predefinidos por GitHub Copilot

| Comando | Qué hace |
|---|---|
| `/explain` | Explica el código seleccionado o el fichero activo |
| `/fix` | Propone una corrección para el error o código seleccionado |
| `/tests` | Genera tests para el código seleccionado |
| `/doc` | Genera documentación / docstrings para el código seleccionado |
| `/new` | Crea un nuevo fichero o proyecto desde cero |
| `/newNotebook` | Crea un nuevo Jupyter Notebook |
| `/clear` | Limpia el historial de la conversación actual |
| `/help` | Muestra ayuda sobre Copilot Chat |

### Cómo se combinan los tres

```
# Corregir un fallo detectado en terminal:
@workspace /fix el test falla — ver #terminalLastCommand

# Generar tests siguiendo las reglas del proyecto:
/tests para #file:entities/coche_combustion.py

# Iniciar una sesión de prácticas con contexto pedagógico:
@workspace empieza la sesión de hoy — contexto en #sesion05-propiedades
```

| Mecanismo | Pregunta que responde | Ejemplo |
|---|---|---|
| `#` | **¿Sobre qué?** (contexto) | `#file`, `#codebase`, `#sesion03-metodos` |
| `@` | **¿Quién responde?** (agente) | `@workspace`, `@terminal` |
| `/` | **¿Cómo responde?** (modo) | `/fix`, `/tests`, `/explain` |

---

## 3. Herramientas (tools) predefinidas del agente

En **modo agente**, Copilot encadena estas herramientas de forma autónoma para resolver tareas complejas. En modo chat normal **no las usa** — solo responde con texto.

### Ficheros y workspace

| Tool | Qué hace |
|---|---|
| `read_file` | Lee el contenido de un fichero |
| `list_dir` | Lista el contenido de un directorio |
| `file_search` | Busca ficheros por patrón glob |
| `grep_search` | Busca texto o regex dentro de ficheros |
| `create_file` | Crea un fichero nuevo |
| `insert_edit_into_file` | Edita un fichero existente |
| `replace_string_in_file` | Reemplaza una cadena exacta en un fichero |
| `delete_file` | Elimina un fichero |

### Terminal

| Tool | Qué hace |
|---|---|
| `run_in_terminal` | Ejecuta un comando de shell |
| `get_terminal_output` | Recupera la salida de un proceso en segundo plano |

### Código y semántica

| Tool | Qué hace |
|---|---|
| `semantic_search` | Búsqueda semántica por significado en el codebase |
| `get_errors` | Obtiene errores de compilación/lint de un fichero |

### IDE / Editor

| Tool | Qué hace |
|---|---|
| `open_file` | Abre un fichero en el editor |
| `show_content` | Muestra contenido renderizado (Markdown, HTML…) en el chat |
| `fetch` | Hace una petición HTTP (para leer docs, APIs externas) |

### Flujo típico del agente en modo autónomo

```
tarea del usuario
      ↓
  semantic_search / grep_search   ← entiende el codebase
      ↓
  read_file                        ← lee los ficheros relevantes
      ↓
  create_file / insert_edit_into_file ← implementa los cambios
      ↓
  run_in_terminal                  ← ejecuta pytest
      ↓
  get_errors / get_terminal_output ← comprueba resultado
      ↓
  insert_edit_into_file            ← corrige si hay errores
      ↓
  responde al usuario
```

---

## 4. Estructura de `.github/` para guiar a Copilot

GitHub Copilot reconoce de forma nativa dos carpetas dentro de `.github/`:

```
.github/
├── copilot-instructions.md     ← reglas globales, siempre activas
├── instructions/               ← activación AUTOMÁTICA por applyTo
│   └── *.instructions.md
└── prompts/                    ← activación MANUAL con #nombre en el chat
    └── *.prompt.md
```

> ⚠️ La carpeta `workflows/` que usa GitHub Actions para CI/CD es diferente y no tiene relación con estas instrucciones para Copilot. No mezclar los conceptos.

---

## 5. Instruction files — activación automática

### Qué son

Ficheros Markdown con extensión `.instructions.md` ubicados en `.github/instructions/`.
Se inyectan automáticamente en el contexto de Copilot cuando el fichero que se está editando coincide con el patrón `applyTo` del frontmatter.

### Frontmatter obligatorio

```markdown
---
applyTo: 'entities/**/*.py'
description: 'Descripción breve del contenido'
---

# Contenido de las instrucciones...
```

### Cómo funciona `applyTo`

Cuando abres o editas un fichero, Copilot comprueba qué instruction files tienen un patrón `applyTo` que coincide con la ruta de ese fichero y los inyecta **sin que tengas que pedirlo**.

| Patrón `applyTo` | Se activa al editar… |
|---|---|
| `'**/*.py'` | Cualquier fichero Python del proyecto |
| `'entities/**/*.py'` | Solo ficheros en `entities/` |
| `'tests/**/*.py'` | Solo ficheros de tests |
| `'README.md'` | Solo el README |

### Varios instruction files activos a la vez

Los patrones se acumulan. Al editar `entities/coche.py` se activan simultáneamente todos los ficheros cuyos `applyTo` coincidan:

```
entities/coche.py  →  architecture.instructions.md  (applyTo: '**/*.py')
                   →  python-conventions.instructions.md (applyTo: '**/*.py')
                   →  entities.instructions.md  (applyTo: 'entities/**/*.py')
```

### Qué poner en cada instruction file

- **Reglas permanentes** que deben respetarse siempre al tocar esa capa.
- **Prohibiciones** explícitas (qué no importar, qué no hacer).
- **Patrones de código** concretos con ejemplos del propio proyecto.
- **Criterios de decisión** (cuándo usar X en lugar de Y).

Lo que **no** debe ir aquí: tareas concretas de un día, contexto pedagógico puntual, instrucciones de una sola vez → eso va en `prompts/`.

---

## 6. Prompt files — invocación manual

### Qué son

Ficheros Markdown con extensión `.prompt.md` ubicados en `.github/prompts/`.
Encapsulan un **prompt reutilizable** que el usuario invoca explícitamente escribiendo `#nombre-del-prompt` en el chat.

### Frontmatter recomendado

```markdown
---
mode: 'agent'
description: 'Descripción breve que aparece en el autocompletado al escribir #'
---

Contenido del prompt...
```

El campo `mode` puede ser:
- `'agent'` — el prompt se ejecuta en modo agente (puede usar tools).
- `'chat'` — se ejecuta como conversación normal.
- `'edit'` — se ejecuta en modo edición de ficheros.

### Cómo invocarlos

En el chat de Copilot, escribir `#` seguido del nombre del fichero (sin extensión ni ruta):

```
@workspace #sesion05-propiedades empieza la sesión de hoy
/tests para #file:entities/coche.py siguiendo #crear-tests
```

### Qué poner en cada prompt file

- **Tareas concretas y repetibles**: generar un diagrama, crear tests para una entidad, hacer una auditoría de arquitectura.
- **Contexto pedagógico por sesión**: qué se trabaja hoy, qué no se debe hacer todavía, instrucciones de tutor.
- **Workflows de inicio**: checklist de lo que hay que hacer al empezar una tarea.

---

## 7. AGENTS.md vs copilot-instructions.md

Son dos ficheros con propósitos complementarios, **no redundantes**. Cada uno tiene una audiencia diferente.

### `.github/copilot-instructions.md`

- **Lo lee:** GitHub Copilot exclusivamente.
- **Cuándo:** En cada conversación, de forma automática.
- **Asume:** Que el agente ya está dentro del IDE y ve el código.
- **Contenido:** Reglas del proyecto + mapa de navegación hacia los `instructions/`.

```markdown
# Instrucciones globales para GitHub Copilot

## Reglas que NUNCA deben violarse
1. `ui` no puede importar `entities`
2. ...

## Mapa de ficheros de contexto
| Fichero | Se activa | Contenido |
|...      | ...       | ...       |
```

### `AGENTS.md` (en la raíz del proyecto)

- **Lo lee:** Otros agentes de IA (OpenAI Codex, Claude, Gemini CLI, Cursor Agent…).
- **Cuándo:** Al iniciar una sesión agéntica en el repo, llegando "en frío".
- **Asume:** Que el agente no sabe nada del proyecto — acaba de clonar el repo.
- **Contenido:** Comandos para arrancar, estructura de carpetas, reglas críticas, qué no tocar.

```markdown
# AGENTS.md

## Comandos esenciales
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pytest
python main.py
python -m pytest -q
```

## Reglas críticas
1. ui/ no puede importar entities/
2. ...
```

### Diferencia clave resumida

| | `copilot-instructions.md` | `AGENTS.md` |
|---|---|---|
| Audiencia | GitHub Copilot | Cualquier agente externo |
| Activación | Automática en cada chat | Al clonar / iniciar sesión |
| Contexto asumido | Agente dentro del IDE | Agente llegando en frío |
| Contenido | Normas de código | Instrucciones operativas |

---

## 8. MCP — ampliar las herramientas del agente

**MCP (Model Context Protocol)** es el estándar abierto de Anthropic (adoptado por Copilot desde 2025) que permite añadir herramientas externas al agente mediante servidores MCP.

### Configuración

Se define en `.vscode/mcp.json` o en la configuración de usuario de VS Code:

```json
{
  "servers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "${env:GITHUB_TOKEN}" }
    }
  }
}
```

### Servidores MCP útiles

| Servidor MCP | Tools que añade |
|---|---|
| `mcp-server-github` | Leer/crear issues, PRs, comentarios en GitHub |
| `mcp-server-postgres` | Consultar una base de datos PostgreSQL |
| `mcp-server-docker` | Gestionar contenedores Docker |
| `mcp-server-fetch` | Navegar URLs y hacer scraping |
| `mcp-server-filesystem` | Acceso ampliado al sistema de ficheros |

> MCP es el equivalente a lo que Cursor o Claude Desktop ofrecen con sus integraciones de herramientas externas, pero estandarizado y portable entre agentes.

---

## 9. Configuración real de este proyecto (Coches2026)

### Estructura completa de `.github/`

```
.github/
├── copilot-instructions.md                         ← reglas globales siempre activas
│
├── instructions/                                   ← ACTIVACIÓN AUTOMÁTICA por applyTo
│   ├── architecture.instructions.md                applyTo: '**/*.py'
│   │   └─ Capas, dependencias unidireccionales, checklist de nueva funcionalidad
│   ├── python-conventions.instructions.md          applyTo: '**/*.py'
│   │   └─ Type hints, nomenclatura, docstrings, orden de imports
│   ├── mermaid.instructions.md                     applyTo: 'README.md'
│   │   └─ Reglas classDiagram (UML) y C4Container
│   ├── entities.instructions.md                    applyTo: 'entities/**/*.py'
│   │   └─ Dominio puro + visibilidad (__privado, _protegido) + @property + setters
│   ├── services.instructions.md                    applyTo: 'services/**/*.py'
│   │   └─ Casos de uso, Resultado obligatorio, gestión de excepciones
│   ├── ui.instructions.md                          applyTo: 'ui/**/*.py'
│   │   └─ Prohibición de importar entities, patrón de llamada a servicios
│   ├── persistence.instructions.md                 applyTo: 'persistence/**/*.py'
│   │   └─ Adaptadores JSON/Pickle, interfaz de repositorio, pathlib
│   └── tests.instructions.md                       applyTo: 'tests/**/*.py'
│       └─ Given/When/Then, mocks en UI, nombrado de tests
│
└── prompts/                                        ← ACTIVACIÓN MANUAL con #nombre
    ├── sesion01-git.prompt.md                      ← Configurar Git, flujo de ramas
    ├── sesion02-clases-esqueleto.prompt.md         ← Esqueletos de clase en entities/
    ├── sesion03-metodos.prompt.md                  ← Métodos de instancia y de clase
    ├── sesion04-herencia.prompt.md                 ← Herencia, super().__init__()
    ├── sesion05-propiedades.prompt.md              ← ABC, @abstractmethod, @property, MRO
    ├── sesion06-sobrecarga-funciones.prompt.md     ← __str__, __repr__, __len__, __bool__
    ├── sesion07-sobrecarga-operadores.prompt.md    ← __eq__, __hash__, __add__, __getitem__
    ├── sesion08-type-hinting.prompt.md             ← PEP 484/526, mypy --strict
    ├── sesion09-excepciones.prompt.md              ← Jerarquía de excepciones propias
    ├── sesion10-ficheros-texto.prompt.md           ← Persistencia JSON/CSV
    ├── sesion11-ficheros-binarios.prompt.md        ← Persistencia Pickle
    └── sesion12-ejecutable.prompt.md               ← PyInstaller --onefile
```

### Qué instruction files se activan según el fichero que editas

| Fichero editado | Instructions activos automáticamente |
|---|---|
| `entities/coche.py` | `architecture` + `python-conventions` + `entities` |
| `services/gestion_concesionario_service.py` | `architecture` + `python-conventions` + `services` |
| `ui/menu.py` | `architecture` + `python-conventions` + `ui` |
| `persistence/coches_repo_json.py` | `architecture` + `python-conventions` + `persistence` |
| `tests/test_entities.py` | `architecture` + `python-conventions` + `tests` |
| `README.md` | `mermaid` |

### Cómo usar los prompts de sesión

Al inicio de cada sesión práctica, en el chat de Copilot:

```
@workspace #sesion04-herencia
```

Copilot cargará el contexto pedagógico de esa sesión: objetivos, tareas del día, restricciones y modo tutor.

---

## 10. Recetas de uso habitual

### Empezar una sesión práctica

```
@workspace #sesion05-propiedades
¿Por dónde empezamos hoy?
```

### Generar o actualizar el diagrama UML

```
@workspace actualiza el diagrama de clases en README.md
con el estado actual del código en entities/
```
*(El instruction file `mermaid.instructions.md` se activa automáticamente al editar README.md)*

### Crear tests para una entidad

```
/tests para #file:entities/coche_combustion.py
```

### Auditar que no se violan las reglas de arquitectura

```
@workspace revisa todos los imports de ui/menu.py
y confirma que no se importa nada de entities/
```

### Corregir un error de la terminal

```
@workspace /fix — ver #terminalLastCommand
```

### Añadir una nueva funcionalidad respetando la arquitectura

```
@workspace quiero añadir la funcionalidad de "reservar un coche".
Sigue el checklist de #file:.github/instructions/architecture.instructions.md
```

### Consultar las reglas de visibilidad antes de diseñar una clase

```
¿Cuándo debo usar @property y cuándo setter en este proyecto?
[Copilot responde con entities.instructions.md activo automáticamente
 si estás editando un fichero de entities/]
```

---

## Apéndice — Comparativa de mecanismos

| Mecanismo | Fichero | Activación | Audiencia | Mejor para |
|---|---|---|---|---|
| Reglas globales | `copilot-instructions.md` | Automática (siempre) | Copilot | Normas del proyecto |
| Reglas por capa | `instructions/*.instructions.md` | Automática (`applyTo`) | Copilot | Restricciones específicas de una capa |
| Tareas reutilizables | `prompts/*.prompt.md` | Manual (`#nombre`) | Copilot | Workflows, sesiones, generadores |
| Guía operativa | `AGENTS.md` | Al clonar el repo | Otros agentes IA | Arrancar el proyecto, comandos |
| Skill externa | Servidor MCP | Configuración `.vscode/mcp.json` | Copilot agente | Integraciones externas (GitHub, DB…) |


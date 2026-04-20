# Skill: Generar diagrama de arquitectura C4 en Mermaid

## Cuándo usar esta skill

Cárgala cuando debas generar o actualizar el diagrama C4 de arquitectura en `README.md`.

---

## Niveles C4 relevantes para este proyecto

- **Nivel 1 – Contexto**: usuario + sistema completo (raramente necesario aquí).
- **Nivel 2 – Contenedores**: las cuatro capas (`ui`, `services`, `entities`, `persistence`). **Este es el nivel habitual.**
- **Nivel 3 – Componentes**: clases dentro de una capa (usar solo si se detalla una capa concreta).

---

## Plantilla Nivel 2 — Contenedores

````mermaid
C4Container
    title Arquitectura C4 (nivel contenedor) — Coches2026

    Person(usuario, "Usuario", "Opera la app por CLI")

    Container_Boundary(sistema, "Coches2026") {
        Container(ui, "UI CLI", "Python / ui/", "Entrada/salida de consola y menús")
        Container(servicios, "Services", "Python / services/", "Orquesta casos de uso")
        Container(dominio, "Entities", "Python / entities/", "Reglas de negocio y modelo de dominio")
        Container(persistencia, "Persistence", "Python / persistence/", "Almacenamiento futuro")
    }

    Rel(usuario, ui, "Usa")
    Rel(ui, servicios, "Invoca casos de uso")
    Rel(servicios, dominio, "Manipula entidades")
    Rel(servicios, persistencia, "Guardará datos", "(futuro)")
````

---

## Reglas para este proyecto

1. **Nunca** dibujar una flecha `ui → dominio`; viola la arquitectura.
2. La capa `persistence` se muestra con nota "(futuro)" hasta que esté implementada.
3. Usar `Container_Boundary` para agrupar todas las capas dentro del sistema.
4. Añadir `UpdateRelStyle` si se quiere colorear una relación para destacarla en documentación.

---

## Errores comunes

- ❌ Usar `graph TD` en lugar de `C4Container` — perderás la semántica C4.
- ❌ Poner lógica de negocio en `ui` y luego reflejarlo en el diagrama — corregir el código, no el diagrama.
- ❌ Omitir `persistence` del diagrama aunque esté vacía — debe aparecer para comunicar la intención arquitectónica.


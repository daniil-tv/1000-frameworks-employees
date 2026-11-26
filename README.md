# AIEmployee

Публичный каталог AI-сотрудников для маркетинга. Каждый сотрудник — самостоятельный устанавливаемый пакет: инструкции, методология, примеры, инструменты и тесты.

## Выберите сотрудника

| Сотрудник | Задачи | Версия |
|---|---|---|
| [SEO Specialist](employees/seo-specialist/README.md) | Семантика, технический аудит, архитектура, SEO-стратегия | 2.1.0 |
| [Copywriter](employees/copywriter/README.md) | Статьи, коммерческие тексты, редактура, корректура | 1.1.0 |

## Установка

Нужны Node.js и установленный Claude Code или Codex. Используйте [Skills CLI](https://github.com/vercel-labs/skills) для выбранного сотрудника.

**Claude Code**

```bash
npx skills add daniil-tv/1000-frameworks-employees --skill seo-specialist -a claude-code
npx skills add daniil-tv/1000-frameworks-employees --skill copywriter -a claude-code
```

**Codex**

```bash
npx skills add daniil-tv/1000-frameworks-employees --skill seo-specialist -a codex
npx skills add daniil-tv/1000-frameworks-employees --skill copywriter -a codex
```

Можно также скопировать целиком каталог нужного сотрудника в .claude/skills/ или .agents/skills/ проекта. Не копируйте только SKILL.md. Для скачивания репозитория используйте Code → Download ZIP.

## Статус качества

Обе версии доступны для использования, но сравнительные испытания на моделях ещё не завершены. Сценарии тестирования и ограничения находятся в каталогах сотрудников. Внешние сервисы требуют собственных доступов; публикация по умолчанию запрещена без разрешения.

## Другие материалы

[AI Skills — отдельные маркетинговые методики](https://github.com/daniil-tv/1000-frameworks-skills)

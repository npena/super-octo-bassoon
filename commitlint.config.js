// Commitlint configuration for enforcing Conventional Commits
// See: https://www.conventionalcommits.org/en/v1.0.0/
// Install (example):
//   npm install --save-dev @commitlint/{config-conventional,cli}
// or use pnpm / yarn equivalents. Integrate via a git hook (e.g. Husky) or CI.

/** @type {import('@commitlint/types').UserConfig} */
module.exports = {
  extends: ['@commitlint/config-conventional'],
  // Parser preset (leave default unless monorepo / custom parser needs)
  // parserPreset: 'conventional-changelog-conventionalcommits',
  rules: {
    // Core format rules
    'header-max-length': [2, 'always', 88], // Align with Black line length
    'body-max-line-length': [2, 'always', 100],
    'footer-max-line-length': [2, 'always', 100],

    // Type & scope
    'type-enum': [
      2,
      'always',
      [
        'feat',
        'feat!',
        'fix',
        'docs',
        'style',
        'refactor',
        'perf',
        'test',
        'build',
        'ci',
        'chore',
        'revert',
        'deps'
      ]
    ],
    'scope-empty': [0, 'never'], // Allow empty scope

    // Subject formatting
    'subject-empty': [2, 'never'],
    'subject-case': [0], // Allow any case to avoid friction

    // Enforce blank line before body/footer if they exist
    'body-leading-blank': [2, 'always'],
    'footer-leading-blank': [2, 'always']
  },
  prompt: {
    messages: {},
    questions: {
      type: {
        description: 'Select the type of change that you are committing'
      },
      scope: {
        description: 'Specify a scope (optional)' // Press enter to skip
      },
      subject: {
        description: 'Write a short, imperative description of the change'
      },
      body: {
        description: 'Provide a longer description (optional)'
      },
      isBreaking: {
        description: 'Are there any breaking changes?'
      },
      breaking: {
        description: 'Describe the breaking changes'
      },
      isIssueAffected: {
        description: 'Does this change affect any open issues?'
      },
      issues: {
        description: 'Add issue references (e.g. #123, #456)'
      }
    }
  }
};

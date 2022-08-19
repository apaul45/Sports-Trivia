const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    supportFile: "./support/e2e.{js,jsx,ts,tsx}",
    specPattern: "./e2e/*.cy.ts",
    baseUrl: "http://localhost:8080/#"
  },
});

describe('Home Page Click', () => {
  it('should navigate to the home page correctly', () => {
    cy.visit('http://localhost:8080/#');
    cy.contains('Home').click();

    cy.location().should((location) => {
      expect(location.href).to.eq('http://localhost:8080/#/home');
    })
  })
});

describe('Browse Questions Click', () => {
  it('should navigate to the browse page correctly', () => {
    cy.visit('http://localhost:8080/#');
    cy.contains('Browse').click();

    cy.location().should((location) => {
      expect(location.href).to.eq('http://localhost:8080/#/questions');
    })
  })
});

describe('Logo Click', () => {
  it('should navigate to the welcome page correctly', () => {
    cy.visit('http://localhost:8080/#');
    cy.contains('Sports Trivia').click();

    cy.location().should((location) => {
      expect(location.href).to.eq('http://localhost:8080/#/');
    })
  })
});
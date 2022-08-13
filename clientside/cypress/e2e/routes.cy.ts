describe('Home Page Click', () => {
    it('should navigate to the home page correctly', () => {
      cy.visit('');
      cy.contains('Home').click();
  
      cy.location().should((location) => {
        expect(location.href).to.eq('http://localhost:8080/#/home');
      })
    })
  });
  
  describe('Browse Questions Click', () => {
    it('should navigate to the browse page correctly', () => {
      cy.visit('');
      cy.contains('Browse').click();
  
      cy.location().should((location) => {
        expect(location.href).to.eq('http://localhost:8080/#/questions');
      })
    })
  });
  
  describe('Logo Click', () => {
    it('should navigate to the welcome page correctly', () => {
      cy.visit('');
      cy.contains('Sports Trivia').click();
  
      cy.location().should((location) => {
        expect(location.href).to.eq('http://localhost:8080/#/');
      })
    })
  });

  describe('Add Questions Page Visit', () => {
    it('should  navigate to the add questions page correctly', () => {
      cy.visit('/questions/add');

      expect(cy.contains('Add Questions'));
    })
  })
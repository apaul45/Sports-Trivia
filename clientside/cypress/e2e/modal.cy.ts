describe('Question Modal Check', () => {
    it('should open the add question modal', () => {
      cy.visit('/questions');
      cy.contains('Add a Question').click();
  
      cy.get('form.q-form.q-gutter-md').should('be.visible');
    });
    it('should close the add question modal', () => {
      cy.visit('/questions');
      cy.contains('Add a Question').click();
      cy.contains('span', 'Cancel').click();

      cy.get('form.q-form.q-gutter-md').should('not.exist');
    });
});

describe('Set Cards Check', () => {
  it('should display the right amount of sets as cards in the home page', () => {
    cy.visit('/home');
    
    cy.request('GET' ,'http://127.0.0.1:8000/set-count').then((response) => {
      cy.get('div.q-card.my-card').should('have.length', response.body);
    })
  });

  it('should display right amount of user cards', () => {
    cy.visit('/home');

    cy.contains('Hi').click();
    cy.contains('Login').click();
    
    cy.request('GET' ,`http://127.0.0.1:8000/sets/apaul21`).then((response) => {
      cy.get('button.q-btn.q-btn-item.non-selectable.no-outline.q-btn--flat.q-btn--round.text-grey-7.q-btn--actionable.q-focusable.q-hoverable').should('have.length', response.body.length);
    });
  });
});
describe('Add Question Modal Check', () => {
    it('should open the add question modal', () => {
      cy.visit('/questions');
      cy.contains('Add a Question').click();
  
      cy.get('body')
      .then(($body) => {
        return ($body.has('form.q-form.q-gutter-md') ? 'form' : 'nothing');
      })
      .then((selector) => {
        // selector is a string that represents
        // the selector we could use to find it
        expect(selector).to.eql('form')
      })
    });
  });
  
  describe('Close Add Question Modal', () => {
    it('should close the add question modal', () => {
      cy.visit('/questions');
      cy.contains('Add a Question').click();
      cy.contains('span', 'Cancel').click();
  
      cy.get('body')
      .then(($body) => {
        return ($body.has('submit') ? 'form' : 'nothing');
      })
      .then((selector) => {
        // selector is a string that represents
        // the selector we could use to find it
        expect(selector).to.eq('nothing');
      });
    });
  });
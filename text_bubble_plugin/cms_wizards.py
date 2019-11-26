from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from .forms import BubbleWizardForm
from .models import TextModel


class TextBubbleWizard(Wizard):
    def get_success_url(self, obj, **kwargs):
        return None


text_bubble_wizard = TextBubbleWizard(
    title="Text Bubble Wizard",
    weight=200,
    form=BubbleWizardForm,
    model=TextModel,
    description="Create a new Text Bubble",
)

wizard_pool.register(text_bubble_wizard)

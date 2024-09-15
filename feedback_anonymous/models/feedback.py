import logging
from odoo import models, fields, api
from textblob import TextBlob

_logger = logging.getLogger(__name__)

class Feedback(models.Model):
    _name = 'feedback.anonymous'
    _description = 'Feedback from anonymous users'

    comment = fields.Text(string='Comments', required=True)
    sentiment = fields.Selection([
        ('positive', 'Positive'),
        ('negative', 'Negative'),
        ('neutral', 'Neutral'),
    ], string='Sentiment', compute='_compute_sentiment', store=True)
    date = fields.Datetime(string='Publication Date', default=fields.Datetime.now) 

    @api.depends('comment')
    def _compute_sentiment(self):

        for record in self:
            if record.comment:
                blob = TextBlob(record.comment)
                polarity = blob.sentiment.polarity
                _logger.info(f"Comment: {record.comment}")
                _logger.info(f"Polarity: {polarity}")

                if polarity > 0:
                    record.sentiment = 'positive'
                elif polarity < 0:
                    record.sentiment = 'negative' 
                else:
                    record.sentiment = 'neutral'
            else:
                record.sentiment = 'neutral'
                

    


import base, text, stdout, JSON

def default_prep_stream (reporter):
  return open(reporter.report.name, 'w')
def default_close_stream (reporter):
  reporter.output.close( )

class Reporter (object):
  """
  """
  def __init__ (self, report):
    ""
    self.report = report
    self.method = get_reporter_map( )[report.fields['reporter']]
    self.output = getattr(self.method, 'get_output_stream', default_prep_stream)(self)

  def serialize (self, data):
    print self.method.__name__, self.method
    return self.method.serialize(data, self)
  def __call__ (self, data):
    self.blob = self.serialize(data)
    self.output.write(self.blob)
    self.close( )
  def close (self):
    getattr(self.method, 'close_output_stream', default_close_stream)(self)
    

def get_reporter_map ( ):
  return dict([(r.__name__.split('.').pop( ).lower( ), r) for r in get_reporters( ) ])

def get_reporters ( ):
  return [ base, text, stdout, JSON ]

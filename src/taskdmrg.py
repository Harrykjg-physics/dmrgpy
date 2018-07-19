from __future__ import print_function
import numpy as np


def setup_task(self,mode="GS",task=dict()):
  select_task(self,mode=mode)
  for key in task: self.task[key] = task[key] # additional arguments
  write_tasks(self) # write the tasks



def select_task(self,mode="GS"):
  """Setup the sweep parameters"""
  task = dict() # dictionary
  if mode=="GS": # default mode
    task["GS"] = "true"
  elif mode=="excited": # default mode
    task["excited"] = "true"
  elif mode=="correlator": # default mode
    task["GS"] = "true"
    task["correlator"] = "true"
  elif mode=="entropy": # default mode
    task["GS"] = "true"
    task["entropy"] = "true"
  elif mode=="dos": # default mode
    task["dos"] = "true"
  elif mode=="spismj": # default mode
    task["spismj"] = "true"
  elif mode=="overlap": # default mode
    task["overlap"] = "true"
  elif mode=="dynamical_correlator": # default mode
    task["dynamical_correlator"] = "true"
#    task["orthogonal_kpm"] = "true"
  else: raise
  self.task = task # initialize




def write_tasks(self):
  fo = open("tasks.in","w")
  fo.write("tasks\n{\n")
  if self.restart: fo.write(" restart = true\n")
  for key in self.task:
    fo.write(key+" = "+self.task[key]+"\n")
  fo.write("}\n")
#("GS = true\ngap = false\ncorrelator = false\n}\n")
  fo.close()

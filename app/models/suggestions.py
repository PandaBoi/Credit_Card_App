# X - user input
# filter users based on features like age, occupation (since these cant change)
# top 10 similar succesful datapoints (can use Faiss if the number of filtered points too big)
# compare with a mean vector of succ members
# display differences using plot or words

# sideshow: plot a 2d or 3d graph showing where they stand in the world
import numpy as np
from numpy.linalg import norm
import os
import pandas as pd

class SuggestionModel():
  def __init__(self, model_path=None, data_path=None, top_k=10,metric='l2'):
    self.model_path = model_path
    self.data_path = data_path
    self.topk = top_k
    self.metric = metric
    self._load_model()
    self._load_data()

  def _load_model(self):
    if self.model_path and os.path.exists(self.model_path):
      self.model = load_model(self.model_path)

  def _load_data(self):
    if self.data_path and os.path.exists(self.data_path):
      self.data = pd.read_csv(self.data_path)
    else:
        raise EOFError("cannot load data")

  def _filter_users(self, fixed_attribs):
    selected_data = self.data[self.data['Credit_Score']=='Good']
    for attrib, val in fixed_attribs.items():
        if selected_data is None:
            selected_data = self.data[self.data[attrib] == val]
        else:
            selected_data = selected_data[selected_data[attrib] == val]

    return selected_data

  def _get_topk_cands(self, inpt):

    filtered_cands = self._filter_users(fixed_attribs={
        'Age': inpt['Age'].values[0],
        inpt['Occupation'].values[0]: 1
    })
    print("inpt",inpt.columns)
    inp_vec = inpt.drop(columns=['Credit_Score','Occupation','disabled','prior_default','visibility','employed'])
    print(inp_vec.columns)
    cand_vecs = filtered_cands[list(inp_vec.columns)]
    
    if inp_vec.ndim <2:
      inp_vec = inp_vec[None,:]
    
    if self.metric =='l2':
      scores = ((cand_vecs-inp_vec)**2).sum(axis=1)
      topk_idxs = np.argsort(scores)[:self.topk]
    elif self.metric =='cosine':
      scores = np.dot(cand_vecs,inp_vec)/(norm(cand_vecs,axis=1)*norm(inp_vec,axis=1))
      topk_idxs = np.argsort(scores)[::-1][:self.topk]
    
    filtered_cands['prox_score'] = scores

    return filtered_cands.iloc[topk_idxs]



  def _load_data(self):
    if os.path.exists(self.data_path):
        self.data = pd.read_csv(self.data_path)
    else:
        raise

  def get_suggestions(self, inpt):

    topk_cands = self._get_topk_cands(inpt)
    topk_cands = topk_cands[[col for col in topk_cands.columns if col in inpt.columns]]
    float_cols = topk_cands.select_dtypes(include=[float]).mean(axis=0)
    cat_cols = topk_cands.select_dtypes(include=[int])
    float_suggestions = float_cols.to_dict()

    return float_suggestions
    
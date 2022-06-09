from app import app
from flask import render_template

score_metric = [
    {'name': 'ndcg'},
    {'name': 'precision'},
    {'name': 'recall'},
    {'name': 'hr'},
    {'name': 'map'},
    {'name': 'mrr'},
]
problem_type = [
    {'name': 'point'},
    {'name': 'pair'},
]
algo_name = [
    {'name': 'multi-vae'},
    {'name': 'ngcf'},
    {'name': 'mf'},
    {'name': 'fm'},
    {'name': 'nfm'},
    {'name': 'neumf'},
    {'name': 'itemknn'},
    {'name': 'pop'},
    {'name': 'slim'},
    {'name': 'puresvd'}
]
dataset_name = [
    {'name': 'ml-100k'},
    {'name': 'ml-1m'},
    {'name': 'ml-10m'},
    {'name': 'netflix'},
    {'name': 'lastfm'},
    {'name': 'bx'},
    {'name': 'amazon-cloth'},
    {'name': 'amazon-book'},
    {'name': 'amazon-music'},
    {'name': 'epinions'},
    {'name': 'yelp'},
    {'name': 'citeulike'},
]
preprocess_methods = [
    {'name': 'origin'},
    {'name': '5filter'},
    {'name': '10filter'},
]
test_methods = [
    {'name': 'tloo (time-aware leave-one-out)'},
    {'name': 'rloo (random leave-one-out)'},
    {'name': 'tsbr (time-aware split-by-ratio)'},
    {'name': 'rsbr (random split-by-ratio)'},
]
val_methods = [
    {'name': 'tloo'},
    {'name': 'loo'},
    {'name': 'tsbr'},
    {'name': 'rsbr'},

]
sample_methods = [
    {'name': 'uniform (uniformly sample)'},
    {'name': 'item-ascd (sampling popular items with low rank)'},
    {'name': 'item-desc (sampling popular item with high rank)'},
]
loss_types = [
    {'name': 'CL (Cross-entropy Loss)'},
    {'name': 'BPR (BPR Loss)'},
    {'name': 'HL (Hinge Loss)'},
    {'name': 'TL (Top-1 Loss)'},
]

weight_initializer = [
    {'name': 'xavier_normal'},
    {'name': 'normal'},
    {'name': 'uniform'},
    {'name': 'xavier_uniform'}
]

optimizer = [
    {'name': 'sgd'},
    {'name': 'adam'},
    {'name': 'adagrad'},
]

early_stop = [
    {'name': True},
    {'name': False},
]

@app.route('/')
@app.route('/test_command')
def main():
    user = {'username':'Daisy'}
    

    return render_template(
        'test_command.html', 
        user=user, 
        score_metric=score_metric,
        problem_type=problem_type,
        algo_name=algo_name,
        dataset_name=dataset_name,
        preprocess_methods=preprocess_methods,
        test_methods=test_methods,
        val_methods=val_methods,
        sample_methods=sample_methods,
        loss_types=loss_types,
        weight_initializer=weight_initializer
    )

@app.route('/tune_command')
def hpo_tuner():
    user = {'username':'Daisy'}
    return render_template(
        'tune_command.html', 
        user=user, 
        score_metric=score_metric,
        problem_type=problem_type,
        algo_name=algo_name,
        dataset_name=dataset_name,
        preprocess_methods=preprocess_methods,
        test_methods=test_methods,
        val_methods=val_methods,
        sample_methods=sample_methods,
        loss_types=loss_types,
        weight_initializer=weight_initializer,
    )
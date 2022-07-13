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
    {'name': 'point-wise'},
    {'name': 'pair-wise'},
]
algo_name = [
    {'name': 'multi-vae'},
    {'name': 'ngcf'},
    {'name': 'mf'},
    {'name': 'fm'},
    {'name': 'nfm'},
    {'name': 'neumf'},
    {'name': 'itemknn'},
    {'name': 'slim'},
    {'name': 'puresvd'}
]
dataset_name = [
    {'name': 'ml-100k'},
    {'name': 'ml-1m'},
    {'name': 'ml-10m'},
    {'name': 'netflix'},
    {'name': 'lastfm'},
    {'name': 'book-x'},
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
    {'name': 'tsbr (time-aware split-by-ratio)'},
    {'name': 'rsbr (random split-by-ratio)'},
    {'name': 'tloo (time-aware leave-one-out)'},
    {'name': 'rloo (random leave-one-out)'},
]
val_methods = [
    {'name': 'tsbr (time-aware split-by-ratio)'},
    {'name': 'rsbr (random split-by-ratio)'},
    {'name': 'tloo (time-aware leave-one-out)'},
    {'name': 'rloo (random leave-one-out)'},

]
sample_methods = [
    {'name': 'uniform (uniformly sample)'},
    {'name': 'low-pop (sampling popular items with low rank)'},
    {'name': 'high-pop (sampling popular item with high rank)'},
]
loss_types = [
    {'name': 'CL (Cross-entropy Loss)'},
    {'name': 'BPR (BPR Loss)'},
    {'name': 'HL (Hinge Loss)'},
    {'name': 'TL (Top-1 Loss)'},
    {'name': 'SL (Square error loss)'}
]

weight_initializer = [
    {'name': 'default'},
    {'name': 'normal'},
    {'name': 'uniform'},
    {'name': 'xavier_normal'},
    {'name': 'xavier_uniform'}
]

optimizer = [
    {'name': 'default'},
    {'name': 'sgd'},
    {'name': 'adam'},
    {'name': 'adagrad'},
]

early_stop = [
    {'name': 'true'},
    {'name': 'false'},
]

@app.route('/')
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
        optimizer=optimizer,
        early_stop=early_stop
    )

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
        weight_initializer=weight_initializer,
        optimizer=optimizer,
        early_stop=early_stop
    )
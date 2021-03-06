import os
import time
import csv
import json
from lettuce import step, world
from subprocess import check_call, CalledProcessError
from bigml.api import check_resource
from bigmler.bigmler import MONTECARLO_FACTOR

@step(r'I create BigML resources uploading train "(.*)" file to test "(.*)" and log predictions in "(.*)"')
def i_create_all_resources(step, data=None, test=None, output=None):
    if data is None or test is None or output is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    try:
        retcode = check_call("bigmler --train " + data + " --test " + test + " --output " + output + " --max-batch-models 1", shell=True)
        if retcode < 0:
            assert False
        else:
            world.test_lines = 0
            for line in open(test, "r"):
                world.test_lines += 1
            world.output = output
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)


@step(r'I create BigML resources using source to test "(.*)" and log predictions in "(.*)"')
def i_create_resources_from_source(step, test=None, output=None):
    if test is None or output is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    try:
        retcode = check_call("bigmler --source " + world.source['resource'] + " --test " + test + " --output " + output, shell=True)
        if retcode < 0:
            assert False
        else:
            world.test_lines = 0
            for line in open(test, "r"):
                world.test_lines += 1
            world.output = output
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)


@step(r'I create BigML resources using dataset to test "(.*)" and log predictions in "(.*)"')
def i_create_resources_from_dataset(step, test=None, output=None):
    if test is None or output is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    try:
        retcode = check_call("bigmler --dataset " + world.dataset['resource'] + " --test " + test + " --output " + output, shell=True)
        if retcode < 0:
            assert False
        else:
            world.test_lines = 0
            for line in open(test, "r"):
                world.test_lines += 1
            world.output = output
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)

@step(r'I create BigML resources using dataset, objective field (.*) and model fields (.*) to test "(.*)" and log predictions in "(.*)"')
def i_create_resources_from_dataset_objective_model(step, objective=None, fields=None, test=None, output=None):
    if objective is None or fields is None or test is None or output is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    try:
        retcode = check_call("bigmler --dataset " + world.dataset['resource'] + " --objective " + objective + " --model-fields " + fields + " --test " + test + " --output " + output, shell=True)
        if retcode < 0:
            assert False
        else:
            world.test_lines = 0
            for line in open(test, "r"):
                world.test_lines += 1
            world.output = output
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)

@step(r'I create BigML resources using model to test "(.*)" and log predictions in "(.*)"')
def i_create_resources_from_model(step, test=None, output=None):
    if test is None or output is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    try:
        retcode = check_call("bigmler --model " + world.model['resource'] + " --test " + test + " --output " + output + " --max-batch-models 1", shell=True)
        if retcode < 0:
            assert False
        else:
            world.test_lines = 0
            for line in open(test, "r"):
                world.test_lines += 1
            world.output = output
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)


@step(r'I create BigML resources using ensemble of (.*) models to test "(.*)" and log predictions in "(.*)"')
def i_create_resources_from_ensemble(step, number_of_models=None, test=None, output=None):
    if number_of_models is None or test is None or output is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    try:
        retcode = check_call("bigmler --dataset " + world.dataset['resource'] + " --test " + test + " --number-of-models " + str(number_of_models) + " --tag my_ensemble --output " + output, shell=True)
        if retcode < 0:
            assert False
        else:
            world.test_lines = 0
            for line in open(test, "r"):
                world.test_lines += 1
            world.output = output
            world.number_of_models = int(number_of_models)
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)


@step(r'I create BigML resources using models in file "(.*)" to test "(.*)" and log predictions in "(.*)"')
def i_create_resources_from_models_file(step, models_file=None, test=None, output=None):
    if models_file is None or test is None or output is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    try:
        retcode = check_call("bigmler --models " + models_file + " --test " + test + " --output " + output, shell=True)
        if retcode < 0:
            assert False
        else:
            world.test_lines = 0
            for line in open(test, "r"):
                world.test_lines += 1
            world.output = output
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)


@step(r'I create BigML resources using dataset in file "(.*)" to test "(.*)" and log predictions in "(.*)"')
def i_create_resources_from_dataset_file(step, dataset_file=None, test=None, output=None):
    if dataset_file is None or test is None or output is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    try:
        retcode = check_call("bigmler --datasets " + dataset_file + " --test " + test + " --output " + output, shell=True)
        if retcode < 0:
            assert False
        else:
            world.test_lines = 0
            for line in open(test, "r"):
                world.test_lines += 1
            world.output = output
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)


@step(r'I create a BigML cross-validation with rate (0\.\d+) using a dataset and log results in "(.*)"')
def i_create_cross_validation_from_dataset(step, rate=None, output=None):
    if rate is None or output is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    world.number_of_models = int(MONTECARLO_FACTOR * float(rate))
    world.number_of_evaluations = world.number_of_models
    try:
        retcode = check_call("bigmler --dataset " + world.dataset['resource'] + " --cross-validation-rate " + rate + " --output " + output, shell=True)
        if retcode < 0:
            assert False
        else:
            world.output = output
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)


@step(r'I combine BigML predictions files in "(.*)" and "(.*)" into "(.*)"')
def i_find_predictions_files(step, directory1=None, directory2=None, output=None):
    if directory1 is None or directory2 is None or output is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    try:
        retcode = check_call("bigmler --combine-votes " + directory1 + "," + directory2 + " --output " + output, shell=True)
        if retcode < 0:
            assert False
        else:
            world.test_lines = 0
            for line in open("%s%spredictions.csv" % (directory1, os.sep), "r"):
                world.test_lines += 1
            world.output = output
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)


@step(r'I combine BigML predictions files in "(.*)" and "(.*)" into "(.*)" with method "(.*)"')
def i_find_predictions_files(step, directory1=None, directory2=None, output=None, method=None):
    if directory1 is None or directory2 is None or output is None or method is None:
        assert False
    world.directory = os.path.dirname(output)
    world.folders.append(world.directory)
    try:
        retcode = check_call("bigmler --combine-votes " + directory1 + "," + directory2 + " --output " + output + " --method " + method, shell=True)
        if retcode < 0:
            assert False
        else:
            world.test_lines = 0
            for line in open("%s%spredictions.csv" % (directory1, os.sep), "r"):
                world.test_lines += 1
            world.output = output
            assert True
    except (OSError, CalledProcessError, IOError) as exc:
        assert False, str(exc)


@step(r'I check that the source has been created')
def i_check_create_source(step):
    source_file = "%s%ssource" % (world.directory, os.sep)
    try:
        source_file = open(source_file, "r")
        source = check_resource(source_file.readline().strip(),
                                world.api.get_source)
        world.sources.append(source['resource'])
        world.source = source
        source_file.close()
        assert True
    except Exception, exc:
        assert False, str(exc)


@step(r'I check that the dataset has been created')
def i_check_create_dataset(step):
    dataset_file = "%s%sdataset" % (world.directory, os.sep)
    try:
        dataset_file = open(dataset_file, "r")
        dataset = check_resource(dataset_file.readline().strip(),
                                 world.api.get_dataset)
        world.datasets.append(dataset['resource'])
        world.dataset = dataset
        dataset_file.close()
        assert True
    except Exception, exc:
        assert False, str(exc)


@step(r'I check that the model has been created')
def i_check_create_model(step):
    model_file = "%s%smodels" % (world.directory, os.sep)
    try:
        model_file = open(model_file, "r")
        model = check_resource(model_file.readline().strip(),
                               world.api.get_model)
        world.models.append(model['resource'])
        world.model = model
        model_file.close()
        assert True
    except Exception, exc:
        assert False, str(exc)

@step(r'I check that the ensemble has been created')
def i_check_create_ensemble(step):
    ensemble_file = "%s%sensemble" % (world.directory, os.sep)
    try:
        ensemble_file = open(ensemble_file, "r")
        ensemble = check_resource(ensemble_file.readline().strip(),
                               world.api.get_ensemble)
        world.ensembles.append(ensemble['resource'])
        world.ensemble = ensemble
        ensemble_file.close()
        assert True
    except Exception, exc:
        assert False, str(exc)

@step(r'I check that the models have been created')
def i_check_create_models(step):
    model_file = "%s%smodels" % (world.directory, os.sep)
    model_ids = []
    number_of_lines = 0
    count = 0
    while world.number_of_models != number_of_lines and count < 10:
        number_of_lines = 0
        for line in open(model_file, "r"):
            number_of_lines += 1
            model_id = line.strip()
            model_ids.append(model_id)
        if world.number_of_models != number_of_lines:
            time.sleep(10)
            count += 1
    if world.number_of_models != number_of_lines:
        assert False, "number of models %s and number of lines in models file %s: %s" % (world.number_of_models, model_file, number_of_lines)
    world.model_ids = model_ids
    for model_id in model_ids:
        try:
            model = check_resource(model_id, world.api.get_model)
            world.models.append(model_id)
            assert True
        except Exception, exc:
            assert False, str(exc)

@step(r'I check that the evaluation has been created')
def i_check_create_evaluation(step):
    evaluation_file = "%s%sevaluation" % (world.directory, os.sep)
    try:
        evaluation_file = open(evaluation_file, "r")
        evaluation = check_resource(evaluation_file.readline().strip(),
                                    world.api.get_evaluation)
        world.evaluations.append(evaluation['resource'])
        world.evaluation = evaluation
        evaluation_file.close()
        assert True
    except:
        assert False


@step(r'I check that the evaluations have been created')
def i_check_create_evaluations(step):
    evaluations_file = "%s%sevaluations" % (world.directory, os.sep)
    evaluation_ids = []
    number_of_lines = 0
    count = 0
    while world.number_of_evaluations != number_of_lines and count < 10:
        number_of_lines = 0
        for line in open(evaluations_file, "r"):
            number_of_lines += 1
            evaluation_id = line.strip()
            evaluation_ids.append(evaluation_id)
        if world.number_of_evaluations != number_of_lines:
            time.sleep(10)
            count += 1
    if world.number_of_evaluations != number_of_lines:
        assert False, "number of evaluations %s and number of lines in evaluations file %s: %s" % (world.number_of_evaluations, evaluation_file, number_of_lines)
    world.evaluation_ids = evaluation_ids
    for evaluation_id in evaluation_ids:
        try:
            evaluation = check_resource(evaluation_id, world.api.get_evaluation)
            world.evaluations.append(evaluation_id)
            assert True
        except Exception, exc:
            assert False, str(exc)


@step(r'I check that the predictions are ready')
def i_check_create_predictions(step):

    previous_lines = -1
    predictions_lines = 0
    while previous_lines != predictions_lines:
        try:
            predictions_file = world.output
            predictions_file = open(predictions_file, "r")
            predictions_lines = 0
            for line in predictions_file:
                predictions_lines += 1
            if predictions_lines == world.test_lines:
                assert True
            else:
                previous_lines = predictions_lines
                time.sleep(10)
            predictions_file.close()
        except Exception, exc:
            assert False, str(exc)


@step(r'the local prediction file is like "(.*)"')
def i_check_predictions(step, check_file):
    predictions_file = world.output
    try:
        predictions_file = csv.reader(open(predictions_file, "U"), lineterminator="\n")
        check_file = csv.reader(open(check_file, "U"), lineterminator="\n")
        for row in predictions_file:
            check_row = check_file.next()
            if len(check_row) != len(row):
                assert False
            for index in range(len(row)):
                dot = row[index].find(".")
                if dot > 0:
                    try:
                        decimal_places = min(len(row[index]), len(check_row[index])) - dot - 1
                        row[index] = round(float(row[index]), decimal_places)
                        check_row[index] = round(float(check_row[index]), decimal_places)    
                    except ValueError:
                        pass
                if check_row[index] != row[index]:
                    print row, check_row
                    assert False
        assert True
    except Exception, exc:
        assert False, str(exc)


@step(r'the cross-validation json model info is like the one in "(.*)"')
def i_check_cross_validation(step, check_file):
    cv_file = "%s/cross_validation.json" % world.directory
    try:
        with open(cv_file, "U") as cv_handler:
            cv_content = json.loads(cv_handler.read())
        with open(check_file, "U") as check_handler:
            check_content = json.loads(check_handler.read())
        if cv_content['model'] == check_content['model']: 
            assert True
        else:
            assert False, "content: %s, check: %s" % (cv_content, check_content)
    except Exception, exc:
        assert False, str(exc)


@step(r'I check that the stored source file exists')
def i_check_stored_source(step):
    try:
        with open("%s%ssource" % (world.directory, os.sep), "r") as source_file:
            source_id = source_file.readline().strip()
            world.sources.append(source_id)
        storage_source_file = "%s%s%s" % (world.directory, os.sep, source_id.replace("/", "_"))
        if os.path.exists(storage_source_file):
            with open(storage_source_file, "r") as storage_source_file:
                world.source = json.loads(storage_source_file.read().strip())
            assert True
        else:
            assert False
    except Exception, exc:
        assert False, str(exc)


@step(r'And the locale of the source is "(.*)"')
def i_check_source_locale(step, bigml_locale):
    try:
        if bigml_locale == world.source['object']["source_parser"]["locale"]:
            assert True
        else:
            assert False
    except KeyError, exc:
        assert False, str(exc)


@step(r'I create BigML resources uploading train "(.*)" file to evaluate and log evaluation in "(.*)"')
def i_create_all_resources_to_evaluate(step, data=None, output=None):
    if data is None or output is None:
        assert False
    try:
        retcode = check_call("bigmler --evaluate --train " + data + " --output " + output, shell=True)
        if retcode < 0:
            assert False
        else:
            world.directory = os.path.dirname(output)
            world.folders.append(world.directory)
            world.output = output
            assert True
    except OSError as e:
        assert False


@step(r'I create a BigML source from file "(.*)" with locale "(.*)" storing results in "(.*)"')
def i_create_all_resources_to_evaluate(step, data=None, locale=None, output=None):
    if data is None or locale is None or output is None:
        assert False
    try:
        retcode = check_call("bigmler --train " + data + " --locale " + locale + " --output " + output + " --no-dataset --no-model --store", shell=True)
        if retcode < 0:
            assert False
        else:
            world.directory = os.path.dirname(output)
            world.folders.append(world.directory)
            world.output = output
            assert True
    except OSError as e:
        assert False


@step(r'I have previously executed "(.*)" or reproduce it with arguments (.*)$')
def i_have_previous_scenario_or_reproduce_it(step, scenario, kwargs):
    scenarios = {'scenario1': [(i_create_all_resources, True), (i_check_create_source, False), (i_check_create_dataset, False), (i_check_create_model, False)],
                 'scenario1_r': [(i_create_all_resources, True), (i_check_create_source, False), (i_check_create_dataset, False), (i_check_create_model, False)],
                 'scenario5': [(i_create_resources_from_ensemble, True), (i_check_create_models, False)], 
                 'scenario_e1': [(i_create_all_resources_to_evaluate, True), (i_check_create_source, False), (i_check_create_dataset, False), (i_check_create_model, False), (i_check_create_evaluation, False)]}
    if os.path.exists("./%s/" % scenario):
        assert True
    else:
        try:
            kwargs = json.loads(kwargs)
        except Exception, exc:
            print str(exc)
        for function, with_args in scenarios[scenario]:
            if with_args:
                function(step, **kwargs)
            else:
                function(step)

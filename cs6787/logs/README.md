day_test_log_full_11-19_02-16-33.csv, day_log_11-19_02-16-33.csv
Namespace(batch_size=200, cuda=True, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=True, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --rotate_data


day_test_log_full_11-21_23-50-17.csv, day_log_11-21_23-50-17.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.05, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .05

fixed to aplly cw_weight to the original grad of last iter, rather than adjusted grad
day_test_log_full_11-22_00-04-20.csv, day_log_11-22_00-04-20.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.2, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .2

day_test_log_full_11-22_00-13-02.csv, day_log_11-22_00-13-02.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.5, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .5

set the cw_weight to the parameters after the first day
day_test_log_full_11-22_00-17-43.csv, day_log_11-22_00-17-43.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.2, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .2

set momentum to zero after first day
day_test_log_full_11-22_00-33-16.csv, day_log_11-22_00-33-16.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.2, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .2

day_test_log_full_11-23_16-26-49.csv, day_log_11-23_16-26-49.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.5, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .5

day_test_log_full_11-23_16-34-20.csv, day_log_11-23_16-34-20.csv
Namespace(batch_size=200, cuda=True, cw_weight=0.9, data='', epoch_days=10.0, epochs=2, epochs_warm=10, include_invalid=False, lr=0.001, predicted_features='temp-10pctl,temp-90pctl,temp-normal', randomize_samples=False, rotate_data=False, test=False, warm_epoch_days=30.0)
main.py --cuda --epochs 2 --epoch_days 10 --warm_epoch_days 30 --epochs_warm 10 --cw_weight .9


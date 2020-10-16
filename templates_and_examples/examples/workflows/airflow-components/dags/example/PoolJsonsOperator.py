from datetime import timedelta
from kaapana.operators.KaapanaBaseOperator import KaapanaBaseOperator, default_registry, default_project


class PoolJsonsOperator(KaapanaBaseOperator):

    def __init__(self,
                 dag,
                 execution_timeout=timedelta(seconds=30),
                 *args, **kwargs
                 ):

        super().__init__(
            dag=dag,
            name='pool-json',
            image="{}{}/example-pool-jsons:0.1.0".format(default_registry, default_project),
            image_pull_secrets=["registry-secret"],
            execution_timeout=execution_timeout,
            *args,
            **kwargs
        )

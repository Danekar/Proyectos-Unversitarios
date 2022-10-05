<?php
$aws_access_key_id='ASIAZL75W6MZZACKWAF5';
$aws_secret_access_key='2R88zAYxggfy5EX+/PgY4d4P+UqKPAeptIyeZuZ2';
$aws_session_token='FwoGZXIvYXdzEEQaDIiL7p7AHVBtexS/wiK9AWl8apO6mrqm39BvYJtEPSzKLIqL1x3vOF9HQn2PkfOE3LDpQZDiTL18Gj4e4KLJSJMbcQ5/oomIkO7gewyrup8GFSUoqelCixzjKMK2PyAhNz7+aAffqIPWh3lK/rAZUQU5iHGEe9VELnJ4RmlkHCwLQM3bJvPyWFIcVxa2eQZDze+nzgesm+tMRyi1mVA0F+3vmD81B9MJThlbcpYhmbjTqRxYO+bq4uwxxBNjRAtEa4ANMeUuLbxlZvoGrCiEufyOBjIthT1RHzFZnjZpiUVv3vfjGGGgrUI6ACbIjkqNoxGIsWLgrzjzbT+40Q55CjE7';
        $lambda_func='s3KeysSearch';
        $payload='{"queryStringParameters": { "ak":"' . $aws_access_key_id . 
                    '", "sk":"' .$aws_secret_access_key .
                    '", "st":"' . $aws_session_token . '" }}';

        $cmd=' AWS_ACCESS_KEY_ID='. $aws_access_key_id .

             ' AWS_SECRET_ACCESS_KEY='. $aws_secret_access_key .

             ' AWS_SESSION_TOKEN='. $aws_session_token . ' aws lambda invoke --region us-east-1 --function-name '. $lambda_func . ' --payload \''. $payload . '\' /tmp/resp.json 2>&1';

        exec( $cmd,$result,$result2);

        header('Access-Control-Allow-Origin: *');

        $result=file_get_contents("/tmp/resp.json");

        $json=json_decode($result,true);

        echo json_encode($json['body']);
//      echo $payload;
?>


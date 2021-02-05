rule _PEiD_Bundle_v1_00___BoB_BobSoft_igazoz
{
	meta:
		description = "PEiD_Bundle v1_00 ___ BoB  BobSoft"
	strings:
		$a = {60E8210200008B44240452486631C06681384D5A75F58B503C813C025045000075E95AC204006089DD89C38B453C8B54287801EA528B522001EA31C9418B348A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

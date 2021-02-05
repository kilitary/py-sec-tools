rule _PEiD_Bundle_v1_00__v1_01___BoB_BobSoft_yyrqak
{
	meta:
		description = "PEiD_Bundle v1_00 _ v1_01 ___ BoB  BobSoft"
	strings:
		$a = {60E8??0200008B44240452486631C06681384D5A75F58B503C813C025045000075E95AC204006089DD89C38B453C8B54287801EA528B522001EA31C9418B348A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

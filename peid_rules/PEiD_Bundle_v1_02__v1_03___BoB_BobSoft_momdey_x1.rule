rule _PEiD_Bundle_v1_02__v1_03___BoB_BobSoft_momdey
{
	meta:
		description = "PEiD_Bundle v1_02 _ v1_03 ___ BoB  BobSoft"
	strings:
		$a = {60E89C00000000000000000000000000000036??????2E??????000000000000000000000000000000000000000001000080000000004B65726E656C33322E44}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

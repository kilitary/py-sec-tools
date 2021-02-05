rule _PEiD_Bundle_v1_02__v1_04___BoB_BobSoft_bfzcpx
{
	meta:
		description = "PEiD_Bundle v1_02 _ v1_04 ___ BoB  BobSoft"
	strings:
		$a = {60E8??00000000000000000000000000000036??????2E??????000000000000000000000000000000000000000001000080000000004B65726E656C33322E44}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

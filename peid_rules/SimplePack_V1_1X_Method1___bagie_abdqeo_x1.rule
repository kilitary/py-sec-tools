rule _SimplePack_V1_1X_Method1___bagie_abdqeo
{
	meta:
		description = "SimplePack V1_1X _Method1_ __ bagie"
	strings:
		$a = {60E8000000005B8D5BFABD????????8B7D3C8D743D008DBEF80000000FB776064E8B471009C0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

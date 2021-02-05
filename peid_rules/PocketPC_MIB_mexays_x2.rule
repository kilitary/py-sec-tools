rule _PocketPC_MIB_mexays
{
	meta:
		description = "PocketPC MIB"
	strings:
		$a = {E8FFBD271400BFAF1800A4AF1C00A5AF2000A6AF2400A7AF??????0C000000001800A48F1C00A58F2000A68F??????0C2400A78F??????0C252040001400BF8F0800E0031800BD27??FFBD271800??AF??00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

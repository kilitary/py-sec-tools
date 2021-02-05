rule _PUNiSHER_V1_5_Demo__FEUERRADER_andfvj
{
	meta:
		description = "PUNiSHER V1_5 Demo __ FEUERRADER"
	strings:
		$a = {3F0000806620??007E20??009220??00A420??00000000004B45524E454C3332}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

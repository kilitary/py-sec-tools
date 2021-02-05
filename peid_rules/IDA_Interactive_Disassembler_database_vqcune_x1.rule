rule _IDA_Interactive_Disassembler_database_vqcune
{
	meta:
		description = "IDA _Interactive Disassembler_ database"
	strings:
		$a = {494441}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

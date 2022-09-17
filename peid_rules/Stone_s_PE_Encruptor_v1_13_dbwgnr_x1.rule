rule _Stone_s_PE_Encruptor_v1_13_dbwgnr
{
	meta:
		description = "Stone_s PE Encruptor v1_13"
	strings:
		$a = {555756525153E8????????5D8BD581}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

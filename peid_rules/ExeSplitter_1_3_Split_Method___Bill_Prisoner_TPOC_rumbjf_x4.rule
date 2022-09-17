rule _ExeSplitter_1_3_Split_Method___Bill_Prisoner_TPOC_rumbjf
{
	meta:
		description = "ExeSplitter 1_3 _Split Method_ __ Bill Prisoner  TPOC"
	strings:
		$a = {E9FE010000??????????????00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

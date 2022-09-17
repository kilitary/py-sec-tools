rule _ExeSplitter_1_0__Bill_Prisoner_TPOC_urmlil
{
	meta:
		description = "ExeSplitter 1_0 __ Bill Prisoner  TPOC"
	strings:
		$a = {E9??????004D5A??00??0000000400??00FFFF0000B8000000000000004000??00000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

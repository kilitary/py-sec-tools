rule _Turbo_Pascal_Desktop_File_joraeo
{
	meta:
		description = "Turbo Pascal Desktop File"
	strings:
		$a = {547572626F2050617363616C204465736B746F70}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

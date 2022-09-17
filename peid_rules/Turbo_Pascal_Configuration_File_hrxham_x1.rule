rule _Turbo_Pascal_Configuration_File_hrxham
{
	meta:
		description = "Turbo Pascal Configuration File"
	strings:
		$a = {547572626F2050617363616C20436F6E66696775726174696F6E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

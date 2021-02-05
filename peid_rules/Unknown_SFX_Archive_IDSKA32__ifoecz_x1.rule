rule _Unknown_SFX_Archive_IDSKA32__ifoecz
{
	meta:
		description = "Unknown SFX Archive _IDSKA32_"
	strings:
		$a = {6964736B613332}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}

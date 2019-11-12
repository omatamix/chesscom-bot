<?php declare(strict_types=1);

namespace ChessComeApiBot;

/**
 * The chess.com bot api config. 
 */
class Config
{
    /** @var string $apiEndpoint The chess.com bot api endpoint. */
    private static $apiEndpoint;

    /**
     * Construct a new chess.com bot api config.
     *
     * @param string $apiToken The api token provided to you by chess.com.
     *
     * @return void Returns nothing.
     */
    public function setApiEndpoint(string $apiToken)
    {
        self::$apiEndpoint = "https://4player-beta.chess.com/bot?token={$apiToken}";
    }

    /**
     * Get the chess.com api endpoint.
     *
     * @return string Returns the chess.com api endpoint.
     */
    public static getApiEndpoint(): string
    {
        return self::$apiEndpoint;
    }
}
